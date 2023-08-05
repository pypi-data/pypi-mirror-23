import numpy
import zipfile
import os
try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

from tslearn.utils import npy3d_time_series_dataset

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def extract_from_zip_url(url, use_cache=True, cache_dir=None, verbose=False):
    """Download a zip file from its URL and unzip it.

    Parameters
    ----------
    url : string
        URL from which to download.
    use_cache : bool (default: True)
        Whether cached files should be used or just overridden.
    cache_dir : str or None (default: None)
        Directory to be used to cache downloaded file and extract it.
    verbose : bool (default: False)
        Whether to print information about the process (cached files used, ...)

    Returns
    -------
    str or None
        Directory in which the zip file has been extracted if the process was successful, None otherwise
    """
    if cache_dir is None:
        cache_dir = os.path.expanduser(os.path.join("~", ".tslearn"))
    if not os.access(cache_dir, os.W_OK):
        cache_dir = os.path.join("/tmp", ".tslearn")
    dataset_dir = os.path.join(cache_dir, "datasets")
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    fname = os.path.basename(url)
    local_zip_fname = os.path.join(dataset_dir, fname)
    if os.path.exists(local_zip_fname) and use_cache:
        if verbose:
            print("File name %s exists, using it." % local_zip_fname)
    else:
        if verbose:
            print("Downloading file %s from URL %s" % (fname, url))
        urlretrieve(url, local_zip_fname)
    extract_dir = os.path.join(dataset_dir, os.path.splitext(fname)[0])
    try:
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)
            zipfile.ZipFile(local_zip_fname, "r").extractall(path=extract_dir)
            if verbose:
                print("Successfully extracted file %s to path %s" % (local_zip_fname, extract_dir))
        else:
            if verbose:
                print("Directory %s already exists, assuming it contains the appropriate data" % extract_dir)
        return extract_dir
    except zipfile.BadZipFile:
        os.rmdir(extract_dir)
        print("Corrupted zip file encountered, aborting.")
        return None


class UCR_UEA_datasets(object):
    """A convenience class to access UCR/UEA time series datasets.

    When using one (or several) of these datasets in research projects, please cite [1]_.

    Parameters
    ----------
    use_cache : bool (default: True)
        Whether a cached version of the dataset should be used, if found.

    Note
    ----
        Downloading the main file is rather time-consuming, hence it is recommended using `use_cache=True` in order to
        only experience long downloading time once and work on a cached version of the datasets after it.

    References
    ----------
    .. [1] A. Bagnall, J. Lines, W. Vickers and E. Keogh, The UEA & UCR Time Series Classification Repository,
       www.timeseriesclassification.com
    """
    def __init__(self, use_cache=True):
        path = extract_from_zip_url("http://www.timeseriesclassification.com/TSC.zip", use_cache=use_cache,
                                    verbose=False)
        if path is None:
            raise ValueError("Dataset could not be loaded properly."
                             "Using cache to re-download it once might fix the issue")
        self._data_dir = os.path.join(path, "TSC Problems")
        self._ignore_list = ["Data Descriptions"]
        self._filenames = {"CinCECGtorso": "CinC_ECG_torso", "CricketX": "Cricket_X", "CricketY": "Cricket_Y",
                           "CricketZ": "Cricket_Z", "FiftyWords": "50words", "Lightning2": "Lighting2",
                           "Lightning7": "Lighting7", "NonInvasiveFetalECGThorax1": "NonInvasiveFetalECG_Thorax1",
                           "NonInvasiveFetalECGThorax2": "NonInvasiveFetalECG_Thorax2",
                           "GunPoint": "Gun_Point", "SonyAIBORobotSurface1": "SonyAIBORobotSurface",
                           "SonyAIBORobotSurface2": "SonyAIBORobotSurfaceII", "SyntheticControl": "synthetic_control",
                           "TwoPatterns": "Two_Patterns", "UWaveGestureLibraryX": "UWaveGestureLibrary_X",
                           "UWaveGestureLibraryY": "UWaveGestureLibrary_Y",
                           "UWaveGestureLibraryZ": "UWaveGestureLibrary_Z", "WordSynonyms": "WordsSynonyms"}
        # File names for datasets for which it is not obvious

    def list_datasets(self):
        """List datasets in the UCR/UEA archive."""
        return [path for path in os.listdir(self._data_dir)
                if os.path.isdir(os.path.join(self._data_dir, path)) and path not in self._ignore_list]

    def load_dataset(self, dataset_name):
        """Load a dataset from the UCR/UEA archive from its name.

        Parameters
        ----------
        dataset_name : str
            Name of the dataset. Should be in the list returned by `list_datasets`

        Returns
        -------
        numpy.ndarray of shape (n_ts_train, sz, d) or None
            Training time series. None if unsuccessful.
        numpy.ndarray of integers with shape (n_ts_train, ) or None
            Training labels. None if unsuccessful.
        numpy.ndarray of shape (n_ts_test, sz, d) or None
            Test time series. None if unsuccessful.
        numpy.ndarray of integers with shape (n_ts_test, ) or None
            Test labels. None if unsuccessful.

        Examples
        --------
        >>> X_train, y_train, X_test, y_test = UCR_UEA_datasets().load_dataset("TwoPatterns")
        >>> print(X_train.shape)
        (1000, 128, 1)
        >>> print(y_train.shape)
        (1000,)
        """
        full_path = os.path.join(self._data_dir, dataset_name)
        if os.path.isdir(full_path) and dataset_name not in self._ignore_list:
            if os.path.exists(os.path.join(full_path, self._filenames.get(dataset_name, dataset_name) + "_TRAIN.txt")):
                fname_train = self._filenames.get(dataset_name, dataset_name) + "_TRAIN.txt"
                fname_test = self._filenames.get(dataset_name, dataset_name) + "_TEST.txt"
                data_train = numpy.loadtxt(os.path.join(full_path, fname_train), delimiter=",")
                data_test = numpy.loadtxt(os.path.join(full_path, fname_test), delimiter=",")
                X_train = npy3d_time_series_dataset(data_train[:, 1:])
                y_train = data_train[:, 0].astype(numpy.int)
                X_test = npy3d_time_series_dataset(data_test[:, 1:])
                y_test = data_test[:, 0].astype(numpy.int)
                return X_train, y_train, X_test, y_test
        return None, None, None, None

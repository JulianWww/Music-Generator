import numpy as np
from scipy.io.wavfile import read as readwave, write as writewav
from os.path import join
from config import U, STEPS

discrete_bins = np.linspace(-1, 1, STEPS, endpoint=0)
reverse_discrete_bins = (discrete_bins + np.concatenate([discrete_bins[1:], [1]]))/2

def load_song(number: int):
    """Load data by numeric Id from the dataset
    
    Args:
        number: the Id of the element of the dataset
    """
    return readwave(join("data", f"{number}.wav"))[1]

def save_song(number: int, data: np.ndarray, rate=48000):
    """Save data by numeric Id from the dataset
    
    Args:
        number: the Id of the element of the dataset
        data: the data to save
        rate: the frame rate of the data
    """
    return writewav(join("data", f"{number}.wav"), rate, data)

def u_law_encode(data: np.ndarray):
    """u law encode the data. This is to reduce the amount of bits the ai needs to output to encode the audio for better computational efficency
    
    Args:
        data: the data to encode
    """
    return np.sign(data)*np.log(1 + U * np.abs(data)) / np.log(1+U)

def u_law_decode(data: np.ndarray):
    """u law decodes the data.
    
    Args:
        data: the data to encode
    """
    return np.sign(data)*((1+U)**np.abs(data)-1) / U

def to_discrete(data: np.ndarray, bins=discrete_bins):
    """Takes the data and splits it into descreet sets
    
    Args:
        data: the data to turn into discreet steps
        bins: The bins to sort it into
    """
    return np.digitize(data, discrete_bins)-1

def to_continuous(data: np.ndarray, bins=reverse_discrete_bins):
    """Takes discrete data and converts it back into discrete data
    
    Args:
        data: the data to tansform
        bins: the reverse of the bins used during discreteization
    """
    return bins[data]

def trim_zeros(arr):
    """Returns a trimmed view of an n-D array excluding any outer
    regions which contain only zeros.
    """
    nz = np.nonzero(arr)  # Indices of all nonzero elements
    arr_trimmed = arr[nz[0].min():nz[0].max()+1,
                    nz[1].min():nz[1].max()+1]
    return arr_trimmed

def preprocess_data(data_id: int):
    """Takes a wav file, performs u-law operation and transforms it into a discrete set and saves the array
    
    Args:
        data_id: the id of the file to transform
    """
    data = to_discrete(u_law_encode(trim_zeros(load_song(data_id)))).astype(np.int8)
    np.save(f"data/{data_id}.npy", data)


preprocess_data(0)
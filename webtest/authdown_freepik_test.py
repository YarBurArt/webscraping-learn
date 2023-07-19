from authdown_freepik import *

from pathlib import Path
from os import walk


def test_isvalid_email():
    res = isvalid_email("co.de-run@email.com")
    assert res
    res2 = isvalid_email("co.@De-run@EmaIl.CoM")
    assert res2 is False


def test_isvalid_url():
    res = isvalid_url("https://ru.freepik.com/")
    assert res
    res2 = isvalid_url("rU.Free_&Pik/com")
    assert res2 is False


def test_sing_in():
    res = sing_in("co.de-run@email.com", "python~test_auth~down")
    assert res is not None


def test_download_url():
    downloads_path = str(Path.home() / "Downloads")
    files = next(walk(downloads_path), (None, None, []))[2]
    download_url('https://ru.freepik.com/free-photo/view-of-city-with-apartment-buildings-and-green-vegetation_43468051.htm#&position=7&from_view=collections')
    files1 = next(walk(downloads_path), (None, None, []))[2]
    assert len(files) < len(files1)


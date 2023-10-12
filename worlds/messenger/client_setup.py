import io
import logging
import os.path
import subprocess
import urllib.request
from shutil import which
from tkinter.messagebox import askyesnocancel
from typing import Any
from zipfile import ZipFile

import requests

from Utils import is_linux, is_windows, messagebox, tuplize_version


def launch_game() -> None:
    """Check the game installation, then launch it"""
    if not (is_linux or is_windows):
        return
    
    def courier_installed() -> bool:
        """Check if Courier is installed"""
        return os.path.exists(os.path.join(folder, "miniinstaller-log.txt"))
    
    def install_courier() -> None:
        """Installs latest version of Courier"""
    
        # can't use latest since courier uses pre-release tags
        courier_url = "https://api.github.com/repos/Brokemia/Courier/releases"
        latest_download = request_data(courier_url)[0]["assets"][-1]["browser_download_url"]
    
        with urllib.request.urlopen(latest_download) as download:
            with ZipFile(io.BytesIO(download.read()), "r") as zf:
                zf.extractall(folder)
    
        working_directory = os.getcwd()
        os.chdir(folder)
        if is_linux:
            mono_exe = which("mono")
            if not mono_exe:
                # download and use mono kickstart
                # this allows steam deck support
                mono_kick_url = "https://github.com/flibitijibibo/MonoKickstart/archive/refs/heads/main.zip"
                target = os.path.join(folder, "monoKickstart")
                with urllib.request.urlopen(mono_kick_url) as download:
                    with ZipFile(io.BytesIO(download.read()), "r") as zf:
                        os.makedirs(target, exist_ok=True)
                        zf.extractall(target)
                installer = subprocess.Popen([os.path.join(target, "precompiled"),
                                              os.path.join(folder, "MiniInstaller.exe")], shell=False)
            else:
                installer = subprocess.Popen([mono_exe, os.path.join(folder, "MiniInstaller.exe")], shell=False)
        else:
            installer = subprocess.Popen(os.path.join(folder, "MiniInstaller.exe"), shell=False)
        failure = installer.wait()
        if failure:
            messagebox("Failure", "Failed to install Courier", True)
            os.chdir(working_directory)
            raise RuntimeError("Failed to install Courier")
        os.chdir(working_directory)
    
        if courier_installed():
            messagebox("Success!", "Courier successfully installed!")
        messagebox("Failure", "Failed to install Courier", True)
        raise RuntimeError("Failed to install Courier")
    
    def mod_installed() -> bool:
        """Check if the mod is installed"""
        return os.path.exists(os.path.join(folder, "Mods", "TheMessengerRandomizerAP", "courier.toml"))
    
    def request_data(url: str) -> Any:
        """Fetches json response from given url"""
        logging.info(f"requesting {url}")
        response = requests.get(url)
        if response.status_code == 200:  # success
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError:
                raise RuntimeError(f"Unable to fetch data. (status code {response.status_code})")
        else:
            raise RuntimeError(f"Unable to fetch data. (status code {response.status_code})")
        return data

    def available_mod_update() -> bool:
        """Check if there's an available update"""
        url = "https://raw.githubusercontent.com/alwaysintreble/TheMessengerRandomizerModAP/archipelago/courier.toml"
        remote_data = requests.get(url).text
        latest_version = remote_data.splitlines()[1].strip("version = \"")

        toml_path = os.path.join(folder, "Mods", "TheMessengerRandomizerAP", "courier.toml")
        with open(toml_path, "r") as f:
            installed_version = f.read().splitlines()[1].strip("version = \"")

        return tuplize_version(latest_version) > tuplize_version(installed_version)

    def install_mod() -> None:
        """Installs latest version of the mod"""
        url = "https://api.github.com/repos/alwaysintreble/TheMessengerRandomizerModAP/releases/latest"
        assets = request_data(url)["assets"]
        release_url = assets[0]["browser_download_url"]
    
        with urllib.request.urlopen(release_url) as download:
            with ZipFile(io.BytesIO(download.read()), "r") as zf:
                zf.extractall(folder)
    
        messagebox("Success!", "Latest mod successfully installed!")
    
    from . import MessengerWorld
    folder = os.path.dirname(MessengerWorld.settings.game_path)
    if not courier_installed():
        should_install = askyesnocancel("Install Courier",
                                        "No Courier installation detected. Would you like to install now?")
        if not should_install:
            return
        install_courier()
    if not mod_installed():
        should_install = askyesnocancel("Install Mod",
                                        "No randomizer mod detected. Would you like to install now?")
        if not should_install:
            return
        install_mod()
    else:
        if available_mod_update():
            should_update = askyesnocancel("Update Mod",
                                           "Old mod version detected. Would you like to update now?")
            if should_update:
                install_mod()
    if is_linux and not which("mono"):  # don't launch the game if we're on steam deck
        return
    os.startfile("steam://rungameid/764790")

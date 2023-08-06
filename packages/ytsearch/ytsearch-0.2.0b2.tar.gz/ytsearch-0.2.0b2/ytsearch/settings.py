#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import collections

import yaml


CONF_DIR = os.path.expanduser('~/.ytsearch')


DEFAULT = '''
keybindings:
    search:
        '1': 'MODE_ORIGINAL'
        '2': 'MODE_PLAYER'
        '3': 'MODE_QUEUE'
        '4': 'MODE_PLAYLIST'
        k: 'MOVE_UP'
        j: 'MOVE_DOWN'
        a: 'PLAY_STREAM_AUDIO'
        v: 'PLAY_STREAM_VIDEO'
        d: 'CACHE_VIDEO'
        n: 'PLAY_NEXT'
        m: 'MODE_PLAYER'
        down: 'MOVE_DOWN'
        up: 'MOVE_UP'
        enter: 'PLAY_STREAM_AUDIO'
        ctrl enter: 'PLAY_STREAM_VIDEO'
        ZZ: 'QUIT'
        qa: 'QUEUE_ADD_AUDIO'
        qv: 'QUEUE_ADD_VIDEO'
        /: 'SEARCH'
        p: 'MODE_EDIT_PLAYLIST'
        c: 'TOGGLE_CONSUME'
        +: 'PLAYLIST_ADD'
        f: 'MODE_FIND'

    player:
        '1': 'MODE_SEARCH'

player:
    command: 'mpv'
    video_args: ['--player-operation-mode=pseudo-gui']
    audio_args: ['--no-video', '--volume', '50']
    show_automatically: true
    size: 5
    quit_key: 'q'

cache: '~/videos/youtube_cache'
'''


class SettingsEditor:
    def __init__(self):
        pass

    def main():
        return None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None


def load_settings():
    '''Loads the settings from disk.
    
    :return: dict: A dictionary of merged settings.
    '''
    user_settings = load_user_settings()
    default_settings = yaml.load(DEFAULT)
    merged = merge_settings(default_settings, user_settings)
    return merged


def merge_settings(default, user):
    '''Merge 2 dictionaries recursively.
    
    :default: dict: The base dictionary to add items to.
    :user: dict: The dictionary to add items from, if they exist.
    :return: dict: The merged contents.
    '''
    for key, value in user.items():
        if (key in default and isinstance(default[key], dict)
        and isinstance(value, collections.Mapping)):
            merge_settings(default[key], value)
        else:
            default[key] = value
    return default


def load_user_settings():
    '''Loads the settings.yaml file.
    
    :return: dict: The settings that were loaded.
    '''
    if not os.path.exists('{}/settings.yaml'.format(CONF_DIR)):
        return {}

    with open('{}/settings.yaml'.format(CONF_DIR)) as f:
        data = f.read() 
    settings = yaml.load(data)
    if settings is None:
        return {}
    return settings


def create_settings():
    '''Creates the settings file so there is something to load.
    
    :return: None
    '''
    with open('{}/settings.yaml'.format(CONF_DIR), 'w') as f:
        f.write(DEFAULT)
    return None


if not os.path.exists(CONF_DIR):
    os.mkdir(CONF_DIR)

cache = load_settings().get('cache', '~/videos/youtube_cache')
if not cache.endswith('/'):
    cache += '/'
CACHE_LOCATION = os.path.expanduser(cache)

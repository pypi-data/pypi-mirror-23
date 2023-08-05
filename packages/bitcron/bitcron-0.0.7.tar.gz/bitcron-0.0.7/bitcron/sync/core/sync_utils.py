# coding: utf8
from __future__ import absolute_import
import os
import json
import datetime
from bitcron.utils import md5_for_file, md5
from bitcron.utils.path import same_slash, join, is_sub_path
from bitcron.utils.file_utils import hide_a_path, delete_file

app_name = 'bitcroncli'

def get_relative_path(filepath, root=None):
    filepath = same_slash(filepath)
    root = same_slash(root)
    relative_path = os.path.split(filepath)[-1]
    if root and filepath.startswith(root+'/'):
        relative_path = filepath.replace(root+'/', '', 1)
    return relative_path



def get_sync_data_folder(root):
    data_path = join(root, '.sync/%s' % app_name)
    return data_path


def make_sure_sync_data_folder(root):
    sync_folder = join(root, '.sync')
    data_folder = get_sync_data_folder(root)
    if not os.path.isdir(data_folder):
        os.makedirs(data_folder)
        hide_a_path(sync_folder)
    return data_folder


def get_sync_log_path(root):
    sync_folder = join(root, '.sync')
    log_path = join(sync_folder, '%s.log' % app_name)
    return log_path

def make_sure_sync_log_path(root):
    make_sure_sync_data_folder(root)
    sync_folder = join(root, '.sync')
    log_path = join(sync_folder, '%s.log' % app_name)
    return log_path


def store_sync_cursor(root, cursor):
    make_sure_sync_data_folder(root)
    sync_folder = join(root, '.sync')
    cursor_path = join(sync_folder, '%s.cursor' % app_name)
    with open(cursor_path, 'w') as f:
        f.write(cursor)


def delete_sync_cursor(root):
    sync_folder = join(root, '.sync')
    cursor_path = join(sync_folder, '%s.cursor' % app_name)
    try:
        delete_file(cursor_path, to_trash=False)
    except:
        pass

def get_sync_cursor(root):
    sync_folder = join(root, '.sync')
    cursor_path = join(sync_folder, '%s.cursor' % app_name)
    if os.path.isfile(cursor_path):
        with open(cursor_path) as f:
            return f.read()
    return ''


# 这个是 md5 对应relative path, 就不会reset了
def get_sync_data_filename(filepath, root):
    relative_path = get_relative_path(filepath, root)
    return md5(relative_path.lower()) # 全小写处理

def get_sync_data_filepath(filepath, root):
    data_folder = make_sure_sync_data_folder(root)
    data_filename = get_sync_data_filename(filepath, root)
    data_filepath = join(data_folder, data_filename)
    return data_filepath


def after_synced(filepath, root, **extra_data):
    filepath = same_slash(filepath)
    if not os.path.exists(filepath):
        return # ignore
    if not is_sub_path(filepath, root):
        return # ignore
    data_path = get_sync_data_filepath(filepath, root)
    now = datetime.datetime.now()
    relative_path = get_relative_path(filepath, root)
    sync_data = dict(
        filepath = relative_path,
        synced_at = now.strftime('%Y-%m-%d %H:%M:%S'),
        md5 = md5_for_file(filepath),
        is_dir = os.path.isdir(filepath),
        is_relative = True
    )
    sync_data.update(extra_data)
    with open(data_path, 'w') as f:
        f.write(json.dumps(sync_data))

    # store the parent folders into the local sync db
    parent_folder = os.path.dirname(filepath)
    parent_data_path = get_sync_data_filepath(parent_folder, root)
    if not os.path.isfile(parent_data_path):
        after_synced(parent_folder, root)



def after_sync_deleted(filepath, root):
    filepath = same_slash(filepath)
    data_path = get_sync_data_filepath(filepath, root)
    if os.path.isfile(data_path):
        try:
            os.remove(data_path)
        except:
            pass


def get_sync_data(filepath, root):
    # get the synced information for a filepath
    # 根据文件的路径，获得对应 md5 文件，里面存储了必要的信息（md5 * synced_at），用于判断当前文件是否需要同步
    filepath = same_slash(filepath)
    data_path = get_sync_data_filepath(filepath, root)
    if os.path.isfile(data_path):
        try:
            with open(data_path) as f:
                data = json.loads(f.read())
                if data.get('is_relative'):
                    # 相对路径，转为绝对路径
                    data['filepath'] = join(root, data['filepath'])
            if isinstance(data, dict):
                return data
        except:
            pass
    return {} # final



def update_sync_data(filepath, root, new_data):
    # 有时候有必要，需要存储一些特殊的字段进去
    filepath = same_slash(filepath)
    data_path = get_sync_data_filepath(filepath, root)
    data = get_sync_data(filepath, root)
    data.update(new_data)
    with open(data_path, 'w') as f:
        f.write(json.dumps(data))










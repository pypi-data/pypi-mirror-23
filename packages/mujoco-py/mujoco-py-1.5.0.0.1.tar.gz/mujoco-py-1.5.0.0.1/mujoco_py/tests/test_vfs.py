from tempfile import NamedTemporaryFile
from mujoco_py import functions
from mujoco_py.cymj import mujoco_pyVFS


def test_vfs():
    ''' Test basic VFS functionality '''
    vfs = mujoco_pyVFS()
    functions.mj_defaultVFS(vfs)
    functions.mj_deleteVFS(vfs)


def test_files():
    ''' Testing handling VFS files '''
    vfs = mujoco_pyVFS()
    functions.mj_defaultVFS(vfs)
    with NamedTemporaryFile() as f:
        name = f.name
        # Try to find file before added -> missing
        assert functions.mj_findFileVFS(vfs, name) == -1
        # Add file -> success
        assert functions.mj_addFileVFS(vfs, '', name) == 0
        # Add file again -> failure, duplicate
        assert functions.mj_addFileVFS(vfs, '', name) == 2
        # Find file -> success (index 0)
        assert functions.mj_findFileVFS(vfs, name) == 0
        # Delete file -> success
        assert functions.mj_deleteFileVFS(vfs, name) == 0
        # Delete file again -> failure, missing
        assert functions.mj_deleteFileVFS(vfs, name) == -1
    # Add a file which does not exist -> failure, missing
    assert functions.mj_addFileVFS(vfs, '', name) == -1

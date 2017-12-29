import os
import os.path as osp

from rl_teacher.tests.video_render_test import TEST_RENDER_DIR
from rl_teacher.video import upload_to_gcs

def test_upload():
    bucket = os.environ.get('RL_TEACHER_GCS_BUCKET')
    assert bucket and bucket.startswith("gs://"), "env variable RL_TEACHER_GCS_BUCKET must be set and start with gs://"

    gcs_path = 'run_20.mp4'
    dest_path = osp.join(bucket, gcs_path)
    upload_to_gcs('/tmp/rl_teacher_vids/Pong-v0/rl-test-1514538629/run_20.mp4', bucket)


if __name__ == '__main__':
    test_upload()

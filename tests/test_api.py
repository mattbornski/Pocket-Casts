import pocketcasts
import pytest
import vcr

PODCAST_UUID = '8b503540-25d2-0134-2f17-737688e4d168'
EPISODE_UUID = 'a9037e26-c0cc-411c-8bb9-ae2fb2cd38fa'

def test_invalid_method(pocket_instance):
    with pytest.raises(Exception):
        pocket_instance._make_req('test', method='INVALID')

def test_invalid_login():
    with pytest.raises(Exception):
        pocketcasts.Pocketcasts('test', 'INVALID')

def test_get_top_charts(pocket_instance):
    response = pocket_instance.get_top_charts()

def test_get_featured(pocket_instance):
    response = pocket_instance.get_featured()

def test_get_trending(pocket_instance):
    response = pocket_instance.get_trending()

def test_get_podcast(pocket_instance):
    response = pocket_instance.get_podcast(PODCAST_UUID)

def test_get_podcast_episodes(pocket_instance):
    response = pocket_instance.get_podcast_episodes(pocket_instance.get_trending()[0])

def test_get_episode(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    pocket_instance.get_episode(pod, EPISODE_UUID)

def test_get_starred(pocket_instance):
    pocket_instance.get_starred()

def test_search_podcasts(pocket_instance):
    pocket_instance.search_podcasts('test')

def test_subscribe_functions(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    pod.subscribed = True
    pod.subscribed = False

def test_get_episode_notes(pocket_instance):
    response = pocket_instance.get_episode_notes(EPISODE_UUID)

def test_get_subscribed_podcasts(pocket_instance):
    response = pocket_instance.get_subscribed_podcasts()

def test_get_new_releases(pocket_instance):
    response = pocket_instance.get_new_releases()

def test_get_in_progress(pocket_instance):
    response = pocket_instance.get_in_progress()

def test_update_playing_status(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    epi = pocket_instance.get_podcast_episodes(pod)[-1]
    epi.playing_status = 3

def test_invalid_update_playing_status(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    epi = pocket_instance.get_podcast_episodes(pod)[-1]
    with pytest.raises(Exception) as context:
        epi.playing_status = 'invalid'
    assert 'Invalid status.' in str(context.value)

def test_update_played_position(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    epi = pocket_instance.get_podcast_episodes(pod)[-1]
    epi.played_up_to = 2

def test_invalid_played_position(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    epi = pocket_instance.get_podcast_episodes(pod)[-1]
    with pytest.raises(Exception) as context:
        epi.played_up_to = 'invalid'
    assert 'Sorry your update failed.' in str(context.value)

def test_update_starred(pocket_instance):
    pod = pocket_instance.get_podcast(PODCAST_UUID)
    epi = pocket_instance.get_podcast_episodes(pod)[-1]
    epi.starred = True
    epi.starred = False

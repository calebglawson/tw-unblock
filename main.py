'''
This file contains the necessary components to mass-unblock / mass-unmute users.
'''

import json

import typer
import tweepy


APP = typer.Typer()


def _make_config():
    '''
    Load the config from a file.
    '''
    config = open('./config.json')
    return json.load(config)


def _make_api(config):
    '''
    Make a Tweepy api object.
    '''
    auth = tweepy.OAuthHandler(
        config.get('consumer_key'),
        config.get('consumer_secret')
    )

    auth.set_access_token(
        config.get('access_token'),
        config.get('access_token_secret')
    )

    api = tweepy.API(
        auth,
        wait_on_rate_limit=True
    )

    return api


@APP.command()
def unblock():
    '''
    Unblock all the users the authenticated user is blocking.
    '''
    api = _make_api(_make_config())

    blocked_users = api.blocks_ids()

    with typer.progressbar(blocked_users, label='Unblocking') as blocked_users_progress:
        for user in blocked_users_progress:
            api.destroy_block(user)

    typer.echo(f'Unblocked {len(blocked_users)} users')


@APP.command()
def unmute():
    '''
    Unmute all the users the authenticated user is muting.
    '''
    api = _make_api(_make_config())

    muted_users = api.mutes_ids()

    with typer.progressbar(muted_users, label='Unmuting') as muted_users_progress:
        for user in muted_users_progress:
            api.destroy_mute(user)

    typer.echo(f'Unmuted {len(muted_users)} users')


if __name__ == "__main__":
    APP()

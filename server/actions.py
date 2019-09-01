from functools import reduce
from settings import INSTALLED_APPS
import pickle
import json

def get_server_actions():
    modules = reduce(
        lambda value, item: value + [__import__(f'{item}.actions')],
        INSTALLED_APPS,
        []
    )
    actions = reduce(
        lambda value, item: value + [getattr(item, 'actions', [])],
        modules,
        []
    )
    actionnames = reduce(
        lambda value, item: value + getattr(item, 'actionnames', []),
        actions,
        []
    )

    # TODO Реализовать на JSON
    # with open('actions.txt', 'wb') as a:
    #     json.dumps(actionnames)

    with open('actions.txt', 'wb') as a:
        pickle.dump(actionnames, a)
get_server_actions()

def resolve(action_name, actions=None):
    with open('actions.txt', 'rb') as actions:
        actions_list = pickle.load(actions)
        for action in actions_list:
            actions_mapping = {
                action.get('action'): action.get('controller')
            }
    return actions_mapping.get(action_name)

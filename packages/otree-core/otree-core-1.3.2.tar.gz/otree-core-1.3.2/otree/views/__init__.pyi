from typing import List
from otree.common import RealWorldCurrency, Currency

## This code is duplicated in several places
# bots/__init__.pyi, views/__init__.pyi, models/__init__.pyi
# importing doesn't seem to work with PyCharm autocomplete

class Session:

    config = None  # type: dict
    vars = None  # type: dict
    def get_participants(self) -> List[Participant]: pass

    # we could make it List[Subsession] but then we have to define Subsession
    # somewhere, because importing doesn't seem to work for pyi autocomplete
    # in pycharm. too much effort for a rarely used method
    def get_subsessions(self) -> List: pass

class Participant:

    session = None # type: Session
    vars = None  # type: dict
    label = None  # type: str
    id_in_session = None  # type: int
    payoff = None  # type: Currency

    # see comment above about importing
    def get_players(self) -> List: pass
    def payoff_plus_participation_fee(self) -> RealWorldCurrency: pass

class WaitPage:
    wait_for_all_groups = False
    group_by_arrival_time = False
    title_text = None
    body_text = None
    template_name = None
    round_number = None  # type: int
    participant = None  # type: Participant
    session = None  # type: Session

    def is_displayed(self) -> bool: pass
    def after_all_players_arrive(self): pass
    def get_players_for_group(self, waiting_players): pass


class Page:
    round_number = None  # type: int
    template_name = None # type: str
    timeout_seconds = None # type: int
    timeout_submission = None # type: dict
    timeout_happened = None # type: bool
    timer_text = None # type: str
    participant = None  # type: Participant
    session = None  # type: Session
    form_model = None #
    form_fields = None  # type: List[str]

    def get_form_fields(self) -> List['str']: pass
    def vars_for_template(self) -> dict: pass
    def before_next_page(self): pass
    def is_displayed(self) -> bool: pass
    def error_message(self, values): pass
    def get_timeout_seconds(self): pass

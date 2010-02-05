"""Setup the myrats application"""
import logging

from myrats import model
from myrats.config.environment import load_environment
from myrats.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup myrats here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)

    log.info("Adding ticket...")
    ticket = model.Ticket()
    ticket.description='Demarre mais affichage absent'

    meta.Session.add(ticket)
    meta.Session.commit()
    log.info("Successfully set up.")

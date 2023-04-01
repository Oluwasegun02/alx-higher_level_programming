#!/usr/bin/python3
<<<<<<< HEAD
"""Start link class to table in database 
=======
"""Start link class to table in database
>>>>>>> 235c45232620011bf37c9ea0a840aab7fedfe9e2
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

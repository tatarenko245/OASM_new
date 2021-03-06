import pytest


@pytest.fixture(scope='session')
def prepared_select_revision_amendments_by_id(cassandra_session):
    cassandra_session.set_keyspace('revision')
    query = 'SELECT * FROM amendments WHERE cpid=? AND ocid=? AND id=?'
    prepared = cassandra_session.prepare(query)
    return prepared


@pytest.fixture(scope='session')
def prepared_select_notice_compiled_release(cassandra_session):
    cassandra_session.set_keyspace('ocds')
    query = 'SELECT * FROM notice_compiled_release WHERE cp_id=? AND oc_id=?'
    prepared = cassandra_session.prepare(query)
    return prepared


@pytest.fixture(scope='session')
def prepared_select_evaluation_award_by_token_entity(cassandra_session):
    cassandra_session.set_keyspace('ocds')
    query = 'SELECT * FROM evaluation_award WHERE cp_id=? AND stage=? AND token_entity=?'
    prepared = cassandra_session.prepare(query)
    return prepared


@pytest.fixture(scope='session')
def prepared_select_evaluation_award_by_cpid(cassandra_session):
    cassandra_session.set_keyspace('ocds')
    query = 'SELECT * FROM evaluation_award WHERE cp_id=?'
    return cassandra_session.prepare(query)


@pytest.fixture(scope='session')
def prepared_select_evaluation_period_by_cpid(cassandra_session):
    cassandra_session.set_keyspace('ocds')
    query = 'SELECT * FROM evaluation_period WHERE cp_id=?'
    return cassandra_session.prepare(query)

  
@pytest.fixture(scope='session')  
def prepared_select_access_tender_by_cpid(cassandra_session):
    cassandra_session.set_keyspace('ocds')
    query = 'SELECT * FROM access_tender WHERE cp_id=?'
    return cassandra_session.prepare(query)
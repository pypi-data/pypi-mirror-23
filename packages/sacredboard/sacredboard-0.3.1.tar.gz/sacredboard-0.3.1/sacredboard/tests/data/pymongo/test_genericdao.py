import bson
import mongomock
import pytest

from sacredboard.app.data.datastorage import Cursor
from sacredboard.app.data.pymongo.genericdao import GenericDAO


@pytest.fixture
def mongo_client():
    client = mongomock.MongoClient()
    db = client.testdb
    db.runs.insert_one({"status": "COMPLETED", "config":
        {"length": None, "n_input": 255, "batch_size": None,
         "dataset_path": "./german-nouns.hdf5", "validation_ds": "validation",
         "log_dir": "./log/rnn500_dropout0.5_lrate1e-4_minibatch_1000steps",
         "seed": 144363069, "dropout_keep_probability": 0.5,
         "max_character_ord": 255, "training_ds": "training", "num_classes": 3,
         "training_steps": 1000, "learning_rate": 0.0001, "hidden_size": 500},
                        "start_time": {"$date": 1476004818913},
                        "_id": bson.ObjectId("57f9efb2e4b8490d19d7c30e"),
                        "info": {}, "resources": [],
                        "host": {"os": "Linux",
                                 "os_info": "Linux-3.16.0-38-generic-x86_64-with-LinuxMint-17.2-rafaela",
                                 "cpu": "Intel(R) Core(TM) i3 CPU       M 370  @ 2.40GHz",
                                 "python_version": "3.4.3",
                                 "python_compiler": "GCC 4.8.4",
                                 "cpu_count": 4,
                                 "hostname": "ntbacer"},
                        "experiment": {"doc": None, "sources": [[
                            "/home/martin/mnt/noun-classification/train_model.py",
                            "86aaa9b81d6e32a181598ed78bb1d7a1"]],
                                       "dependencies": [["h5py", "2.6.0"],
                                                        ["numpy", "1.11.2"],
                                                        ["sacred", "0.6.10"]],
                                       "name": "German nouns"},
                        "heartbeat": {"$date": 1479211200000},
                        "result": 2403.52, "artifacts": [], "comment": "",
                        "stop_time": {"$date": 1476009883302},
                        "captured_out": "Output: \n"})

    db.runs.insert_one({
        "stop_time": {"$date": 1477853779971},
        "start_time": {"$date": 1477853779941}, "meta": {},
        "_id": bson.ObjectId("58163443b1758523257c69ca"), "resources": [],
        "experiment": {"repositories": [], "name": "pokus", "sources": [
            ["pokus.py", {"$oid": "58163443b1758523257c69c8"}]],
                       "dependencies": ["numpy==1.11.2", "sacred==0.7b0"],
                       "base_dir": "/media/sf_Martin/Documents/archiv/archiv/\u0161kola/\u010cVUT/Magistr/Diplomka/sandbox"},
        "status": "COMPLETED", "config": {"seed": 185616783}, "result": None,
        "host": {"os": ["Linux",
                        "Linux-3.19.0-32-generic-x86_64-with-debian-jessie-sid"],
                 "cpu": "Intel(R) Core(TM) i7-6600U CPU @ 2.60GHz",
                 "python_version": "3.5.2",
                 "hostname": "martin-virtual-machine"},
        "format": "MongoObserver-0.7.0",
        "captured_out": "INFO - pokus - Running command 'run'\nINFO - pokus - Started run with ID \"58163443b1758523257c69ca\"\n",
        "artifacts": [], "command": "run",
        "info": {"tensorflow": {"logdirs": ["./log/test_dir"]}},
        "heartbeat": {"$date": 1477853779970}}
    )
    assert len(list(db.runs.find())) == 2
    return client


def test_find_record(mongo_client):
    generic_dao = GenericDAO(mongo_client, "testdb")
    r = generic_dao.find_record("runs", {"_id": "NON_EXISTING_ID"})
    assert r is None

    r = generic_dao.find_record("runs",
                                {"_id": bson.ObjectId(
                                    "58163443b1758523257c69ca")})
    assert r is not None
    assert r["config"] is not None
    assert r["config"]["seed"] == 185616783

    r = generic_dao.find_record("runs", {"config.learning_rate": 0.0001})
    assert r is not None
    assert r["config"] is not None
    assert r["config"]["seed"] == 144363069


def test_find_records(mongo_client):
    generic_dao = GenericDAO(mongo_client, "testdb")
    r = generic_dao.find_records("EMPTY_COLLECTION")
    assert isinstance(r, Cursor)
    assert r.count() == 0
    assert len(list(r)) == 0

    # Existing collection
    generic_dao = GenericDAO(mongo_client, "testdb")
    runs = list(generic_dao.find_records("runs"))
    assert len(runs) == 2
    assert runs[0]["host"]["hostname"] == "ntbacer"
    assert runs[1]["host"]["hostname"] == "martin-virtual-machine"


def test_find_records_limit(mongo_client):
    generic_dao = GenericDAO(mongo_client, "testdb")
    runs = list(generic_dao.find_records("runs", limit=1))
    assert len(runs) == 1, ""
    assert runs[0]["host"]["hostname"] == "ntbacer"


def test_find_records_order(mongo_client):
    generic_dao = GenericDAO(mongo_client, "testdb")
    runs = list(
        generic_dao.find_records("runs", sort_by="host.python_version"))
    assert len(runs) == 2
    assert runs[0]["host"]["python_version"] == "3.4.3"
    assert runs[1]["host"]["python_version"] == "3.5.2"

    runs = list(generic_dao.find_records("runs", sort_by="host.python_version",
                                         sort_direction="desc"))
    assert len(runs) == 2
    assert runs[0]["host"]["python_version"] == "3.5.2"
    assert runs[1]["host"]["python_version"] == "3.4.3"


filter1 = {"host.os": "Linux", "host.hostname": "ntbacer"}
filter2 = {"result": 2403.52}


@pytest.mark.parametrize("filter", (filter1, filter2))
def test_find_records_filter(mongo_client, filter):
    generic_dao = GenericDAO(mongo_client, "testdb")
    runs = list(generic_dao.find_records("runs", query=filter))
    assert len(runs) == 1
    assert runs[0]["host"]["hostname"] == "ntbacer"

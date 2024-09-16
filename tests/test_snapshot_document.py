# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_kv_objects.db.snapshot.document import SnapshotDocument
from datetime import datetime


def test_snapshot_document_setup():
    s = SnapshotDocument()
    assert s is not None
    # assert s.person_id == "1"
    # assert s.volume_id == "1"
    # assert len(c.roles) == 1
    assert isinstance(s.created_at, datetime)
    assert s.created_by == "system"
    assert isinstance(s.updated_at, datetime)
    assert s.updated_by == "system"
    assert s.deleted_at is None
    assert s.deleted_by is None

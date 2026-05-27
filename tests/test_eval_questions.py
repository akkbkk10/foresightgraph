"""
Tests for evaluation questions utility.
"""

import json
import tempfile
import os
from src.foresightgraph.eval_questions import load_jsonl_questions, validate_question_record


def test_load_valid_jsonl():
    """Test loading valid JSONL file."""
    # Create a temporary JSONL file
    content = '''{"question_id": "mhq_001", "question": "Test question 1", "answer_path": [], "ground_truth_evidence": [], "expected_answer": "answer 1"}
{"question_id": "mhq_002", "question": "Test question 2", "answer_path": [], "ground_truth_evidence": [], "expected_answer": "answer 2"}'''
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
        f.write(content)
        temp_file = f.name
    
    try:
        questions = load_jsonl_questions(temp_file)
        assert len(questions) == 2
        assert questions[0]['question_id'] == 'mhq_001'
        assert questions[1]['question_id'] == 'mhq_002'
    finally:
        os.unlink(temp_file)


def test_load_invalid_jsonl():
    """Test loading JSONL file with invalid JSON."""
    content = '''{"question_id": "mhq_001", "question": "Test question 1", "answer_path": [], "ground_truth_evidence": [], "expected_answer": "answer 1"}
{"question_id": "mhq_002", "question": "Test question 2", "answer_path": [], "ground_truth_evidence": [], "expected_answer": "answer 2"'''
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
        f.write(content)
        temp_file = f.name
    
    try:
        try:
            load_jsonl_questions(temp_file)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "Invalid JSON" in str(e)
    finally:
        os.unlink(temp_file)


def test_load_empty_lines_jsonl():
    """Test loading JSONL file with empty lines."""
    content = '''{"question_id": "mhq_001", "question": "Test question 1", "answer_path": [], "ground_truth_evidence": [], "expected_answer": "answer 1"}

{"question_id": "mhq_002", "question": "Test question 2", "answer_path": [], "ground_truth_evidence": [], "expected_answer": "answer 2"}'''
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
        f.write(content)
        temp_file = f.name
    
    try:
        questions = load_jsonl_questions(temp_file)
        assert len(questions) == 2
        assert questions[0]['question_id'] == 'mhq_001'
        assert questions[1]['question_id'] == 'mhq_002'
    finally:
        os.unlink(temp_file)


def test_validate_valid_record():
    """Test validating a valid question record."""
    record = {
        "question_id": "mhq_001",
        "question": "Test question",
        "answer_path": [],
        "ground_truth_evidence": [],
        "expected_answer": "Test answer"
    }
    
    assert validate_question_record(record) is True


def test_validate_missing_required_fields():
    """Test validating a record with missing required fields."""
    record = {
        "question_id": "mhq_001",
        "question": "Test question",
        "answer_path": [],
        "ground_truth_evidence": []
        # missing expected_answer
    }
    
    assert validate_question_record(record) is False


def test_validate_non_dict_record():
    """Test validating a non-dict record."""
    try:
        validate_question_record("not a dict")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Question record must be a dictionary" in str(e)


def test_validate_invalid_field_types():
    """Test validating a record with invalid field types."""
    record = {
        "question_id": 123,  # should be string
        "question": "Test question",
        "answer_path": [],
        "ground_truth_evidence": [],
        "expected_answer": "Test answer"
    }
    
    assert validate_question_record(record) is False


def test_validate_missing_fields():
    """Test validating a record with completely missing fields."""
    record = {
        "question_id": "mhq_001"
        # missing all other required fields
    }
    
    assert validate_question_record(record) is False
"""
Minimal evaluation utility for golden-set questions.

This module provides functionality to load and validate multi-hop question JSONL files
for evaluation purposes.
"""

import json
from typing import Dict, Any, List


def load_jsonl_questions(path: str) -> List[Dict[str, Any]]:
    """
    Load questions from a JSONL file.
    
    Args:
        path: Path to the JSONL file
        
    Returns:
        List of question records
        
    Raises:
        ValueError: If the file contains invalid JSON or records
    """
    questions = []
    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                questions.append(record)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {line_num}: {e}")
    return questions


def validate_question_record(record: Any) -> bool:
    """
    Validate a question record.
    
    Args:
        record: Question record to validate
        
    Returns:
        True if record is valid, False otherwise
        
    Raises:
        ValueError: If record is not a dictionary
    """
    if not isinstance(record, dict):
        raise ValueError("Question record must be a dictionary")
    
    required_fields = [
        'question_id',
        'question', 
        'answer_path',
        'ground_truth_evidence',
        'expected_answer'
    ]
    
    for field in required_fields:
        if field not in record:
            return False
    
    # Additional validation for required fields
    if not isinstance(record['question_id'], str):
        return False
    
    if not isinstance(record['question'], str):
        return False
        
    if not isinstance(record['answer_path'], list):
        return False
        
    if not isinstance(record['ground_truth_evidence'], list):
        return False
        
    if not isinstance(record['expected_answer'], str):
        return False
    
    return True
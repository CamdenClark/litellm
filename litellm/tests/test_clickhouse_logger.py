import asyncio
import io
import os
import sys

# import logging
# logging.basicConfig(level=logging.DEBUG)
sys.path.insert(0, os.path.abspath("../.."))
print("Modified sys.path:", sys.path)


import logging

import litellm
from litellm import completion
from litellm._logging import verbose_logger

litellm.num_retries = 3

import random
import time

import pytest


@pytest.mark.asyncio
@pytest.mark.skip(reason="beta test - this is a new feature")
async def test_custom_api_logging():
    try:
        litellm.success_callback = ["clickhouse"]
        litellm.set_verbose = True
        verbose_logger.setLevel(logging.DEBUG)
        await litellm.acompletion(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"This is a test"}],
            max_tokens=10,
            temperature=0.7,
            user="ishaan-2",
        )

    except Exception as e:
        pytest.fail(f"An exception occurred - {e}")
    finally:
        # post, close log file and verify
        # Reset stdout to the original value
        print("Passed!")

"""Expose the package's root agent.

The ADK expects each agent package to expose a ``root_agent`` object at the
package level.  The previous implementation only imported the ``agent`` module
which forced consumers to access ``prompt_validation_agent.agent.root_agent``.
This made agent discovery fail in contexts that expect the variable to be
available directly on the package.  By importing ``root_agent`` here we make it
available as ``prompt_validation_agent.root_agent`` and restore the expected
behaviour.
"""

from .agent import root_agent

__all__ = ["root_agent"]


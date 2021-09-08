import argparse
from unittest.mock import call, patch

import pytest

from em import cli, copier


@pytest.mark.parametrize(
    "test_name",
    [
        "star",
        ":star:",
    ],
)
@patch("em.argparse.ArgumentParser.parse_args")
@patch("em.sys.exit")
@patch("builtins.print")
def test_star(mock_print, mock_exit, mock_argparse, test_name):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=[test_name], no_copy=None, search=None
    )

    # Act
    cli()

    # Assert
    if copier:
        mock_print.assert_called_once_with("Copied! ⭐")
    else:
        mock_print.assert_called_once_with("⭐")


@patch("em.argparse.ArgumentParser.parse_args")
@patch("em.sys.exit")
@patch("builtins.print")
def test_not_found(mock_print, mock_exit, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["xxx"], no_copy=None, search=None
    )

    # Act
    cli()

    # Assert
    mock_print.assert_called_once_with("")


@patch("em.argparse.ArgumentParser.parse_args")
@patch("em.sys.exit")
@patch("builtins.print")
def test_no_copy(mock_print, mock_exit, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["star"], no_copy=True, search=None
    )

    # Act
    cli()

    # Assert
    mock_print.assert_called_once_with("⭐")


@patch("em.argparse.ArgumentParser.parse_args")
@patch("em.sys.exit")
@patch("builtins.print")
def test_search_star(mock_print, mock_exit, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["star"], no_copy=None, search=True
    )
    expected = (
        "💫  dizzy",
        "⭐  star",
        "✳️  eight_spoked_asterisk",
    )

    # Act
    cli()

    # Assert
    for arg in expected:
        assert call(arg) in mock_print.call_args_list

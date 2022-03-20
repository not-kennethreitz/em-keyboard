import argparse
import random
from unittest.mock import call, patch

import pytest

from em import cli, copier


@pytest.mark.parametrize(
    "test_name",
    [
        "star",
        ":star:",
        "STAR",
        ":Star:",
    ],
)
@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_star(mock_print, mock_argparse, test_name):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=[test_name], no_copy=None, search=False, random=False
    )

    # Act
    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    if copier:
        mock_print.assert_called_once_with("Copied! ⭐")
    else:
        mock_print.assert_called_once_with("⭐")
    assert e.type == SystemExit
    assert e.value.code == 0


@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_not_found(mock_print, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["xxx"], no_copy=None, search=False, random=False
    )

    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    mock_print.assert_called_once_with("")
    assert e.type == SystemExit
    assert e.value.code == 1


@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_no_copy(mock_print, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["star"], no_copy=True, search=False, random=False
    )

    # Act
    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    mock_print.assert_called_once_with("⭐")
    assert e.type == SystemExit
    assert e.value.code == 0


@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_search_star(mock_print, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["star"], no_copy=None, search=True, random=False
    )
    expected = (
        "💫  dizzy",
        "⭐  star",
        "✳️  eight_spoked_asterisk",
    )

    # Act
    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    for arg in expected:
        assert call(arg) in mock_print.call_args_list
    assert e.type == SystemExit
    assert e.value.code == 0


@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_search_single_result_is_copied(mock_print, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["ukraine"], no_copy=None, search=True, random=False
    )

    # Act
    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    if copier:
        mock_print.assert_called_once_with("Copied! 🇺🇦  flag_ukraine")
    else:
        mock_print.assert_called_once_with("🇺🇦  flag_ukraine")
    assert e.type == SystemExit
    assert e.value.code == 0


@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_search_not_found(mock_print, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=["twenty_o_clock"], no_copy=None, search=True, random=False
    )

    # Act
    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    mock_print.assert_not_called()
    assert e.type == SystemExit
    assert e.value.code == 1


@patch("em.argparse.ArgumentParser.parse_args")
@patch("builtins.print")
def test_random(mock_print, mock_argparse):
    # Arrange
    mock_argparse.return_value = argparse.Namespace(
        name=None, no_copy=None, search=False, random=True
    )
    random.seed(123)

    # Act
    with pytest.raises(SystemExit) as e:
        cli()

    # Assert
    if copier:
        mock_print.assert_called_once_with("Copied! 😽  kissing_cat")
    else:
        mock_print.assert_called_once_with("😽  kissing_cat")
    assert e.type == SystemExit
    assert e.value.code == 0

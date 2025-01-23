from __future__ import annotations

import random
import shlex

import pytest

from em import cli, try_copy_to_clipboard  # type: ignore[import-untyped]

copier_deps_installed = try_copy_to_clipboard("checking if copy works")


@pytest.mark.parametrize(
    "test_name",
    [
        "star",
        ":star:",
        "STAR",
        ":Star:",
    ],
)
def test_star(capsys: pytest.LogCaptureFixture, test_name: str) -> None:
    # Act
    ret = cli.main(shlex.split(test_name))

    # Assert
    output = capsys.readouterr().out.rstrip()
    if copier_deps_installed:
        assert output == "Copied! ⭐"
    else:
        assert output == "⭐"
    assert ret == 0


def test_not_found(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "xxx --no-copy"

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    assert output == ""
    assert ret != 0


def test_no_copy(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "star --no-copy"

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    assert output == "⭐"
    assert ret == 0


def test_search_star(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--search star"
    expected = (
        "💫  dizzy",
        "⭐  star",
        "✳️  eight_spoked_asterisk",
    )

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    for arg in expected:
        assert arg in output
    assert ret == 0


def test_search_single_result_is_copied(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--search ukraine"

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    if copier_deps_installed:
        assert output == "Copied! 🇺🇦  flag_ukraine"
    else:
        assert output == "🇺🇦  flag_ukraine"
    assert ret == 0


def test_search_not_found(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--search twenty_o_clock"

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    assert output == ""
    assert ret != 0


def test_search_multi_word(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--search big tent"

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    if copier_deps_installed:
        assert output == "Copied! 🎪  circus_tent"
    else:
        assert output == "🎪  circus_tent"
    assert ret == 0


def test_random(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--random"
    random.seed(123)

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    if copier_deps_installed:
        assert output == "Copied! 😽  kissing_cat"
    else:
        assert output == "😽  kissing_cat"
    assert ret == 0


def test_random_no_copy(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--random --no-copy"
    random.seed(123)

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    assert output == "😽  kissing_cat"
    assert ret == 0


def test_no_name(capsys: pytest.LogCaptureFixture) -> None:
    # Arrange
    args = "--search"

    # Act
    ret = cli.main(shlex.split(args))

    # Assert
    output = capsys.readouterr().out.rstrip()
    assert output == ""
    assert ret != 0

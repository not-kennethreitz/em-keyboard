# Release Checklist

- [ ] Get `main` to the appropriate code release state.
      [GitHub Actions](https://github.com/hugovk/em-keyboard/actions) should be running
      cleanly for all merges to `main`.
      [![GitHub Actions status](https://github.com/hugovk/em-keyboard/workflows/Test/badge.svg)](https://github.com/hugovk/em-keyboard/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/hugovk/em-keyboard/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/hugovk/em-keyboard/actions?query=workflow%3ADeploy)
      has deployed to [PyPI](https://pypi.org/project/em-keyboard/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y em-keyboard && pip3 install -U em-keyboard && em rocket
```

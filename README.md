# Executor One

## Running `executor.py`

Run the commands from the repository root, the folder containing `executor.py`:

```bash
cd /Users/roopasingh/Desktop/Shiva/PythonAlgo/repo/Executor_One
```

### Run one logic

```bash
python3 executor.py \
  --userinterface gsheet \
  --key ../bankniftyorb-2b0a4e15319b.json \
  --logic vwap_piercing_options_buy
```

The equivalent logic name `vwap_piercing_options` is also supported.

### Run multiple logics

Pass multiple logic names after one `--logic` option:

```bash
python3 executor.py \
  --userinterface gsheet \
  --key ../bankniftyorb-2b0a4e15319b.json \
  --logic vwap_piercing_options vwap_piercing_options_buy
```

### Available logic names

- `example`
- `vwap_piercing_options`
- `vwap_piercing_options_buy`

### Arguments

- `--userinterface`: User interface to use. Currently supported: `gsheet`.
- `--key`: Path to the broker credentials JSON file.
- `--logic`: One or more registered logic names.

To see all options:

```bash
python3 executor.py --help
```

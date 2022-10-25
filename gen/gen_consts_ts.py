import json
import sys

preamble = '''
export const NUM_BOARDS = 32;

export const NUM_GUESSES = 37;

export const PRACTICE_MODE_MIN_ID = 100000;

export const START_DATE = (() => {
  // Use this method so that the start date is offset by current timezone offset
  // Old method had problems with the start date being before DST
  const utcDate = new Date("2022-03-03T00:00:00Z").getTime();
  const offset = new Date().getTimezoneOffset();
  return utcDate + offset * 60 * 1000;
})();

export const ALPHABET = new Set([
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
]);
'''

def _main(target, valid, out):
    with open(target) as f:
        target_words = json.load(f)
    with open(valid) as f:
        valid_words = json.load(f)

    print(f'There are {len(target_words)} target words and {len(valid_words)} valid words.')
    with open(out, 'w') as f:
        f.write(preamble)
        f.write('\n\n')
        f.write('export const WORDS_TARGET = [\n')
        for word in target_words:
            f.write(f'  "{word}",\n')
        f.write('];\n\n\n')
        f.write('export const WORDS_VALID = new Set([\n')
        for word in valid_words:
            f.write(f'  "{word}",\n')
        f.write(']);\n')

def main():
    try:
        [target, valid, out] = sys.argv[1:]
        print(f'Generating {out}...')
    except:
        print("usage: python3 gen_consts_ts.py target_words_json_path valid_words_json_path out_ts_path")
        sys.exit(1)
    _main(target, valid, out)

main()

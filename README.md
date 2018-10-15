# Practice Blockchain using python

This is a personal fantasy project and is not intented for any production use.

> Python3 has been aliased to python

# simple.py

```bash
python simple.py
```

Generate random 20 blocks and print to terminal


# simple_with_mining.py

```bash
python simple_with_mining.py
```

This will start the python flask server on port 5000

### Mine a block

Mining a block using proof-of-work where the proof is

> a number which is both divisible by 9 and divisible by the last block's proof

```
[GET] http://localhost:5000/mine
```

### View All blocks

```
[GET] http://localhost:5000/blocks
```

# pathfinding-repair

Code for using pathfinding to repair levels.

Base code and levels in TheVGLC folder from the Video Game Level Corpus: https://github.com/TheVGLC/TheVGLC


## Examples

Check / repair Mario:

```
python3 repair/test_level_mod.py repair/SMB_mod.json example-mario.lvl
python3 repair/test_level_mod.py repair/SMB_mod.json example-mario.lvl --modify
```

Check / repair Kid Icarus:

```
python3 repair/test_level_mod.py repair/KI_mod.json example-kidicarus.lvl
python3 repair/test_level_mod.py repair/KI_mod.json example-kidicarus.lvl --modify
```

Generate levels:

```
python3 grams/grams_simple.py --gramsize 3 --levelsize 100 --solid 'XQS?Bb[]<>' TheVGLC/Super_Mario_Bros/Processed/mario-1-1.txt
python3 grams/grams_simple.py --gramsize 2 --levelsize 100 --solid '#DTX' --transpose TheVGLC/Kid_Icarus/Processed/kidicarus_1.txt
```


## Related Publications

* Seth Cooper and Anurag Sarkar. 2020. "Pathfinding agents for platformer level repair." Proceedings of the Experimental AI in Games Workshop. https://ceur-ws.org/Vol-2862/paper6.pdf

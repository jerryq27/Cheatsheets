# Vim

Vim is a terminal based editor available in most Linux systems.

[Checkpoint (Using Visual Mode)](https://danielmiessler.com/study/vim/)

## Basics

Vim operates by using various modes:

* Command - Keys are interpreted as commands
* Insert - Allows for normal text input
    * `i`/`a` - switch to insert mode at/after the cursor's position
    * `I`/`A` - switch to insert mode at the beginning/end of the line
* Visual - Allows you to select text and apply commands to them
    * `v` - switch to visual mode with character highlighting (can be used with targeted [Text Objects](#Text%20Objects)
    * `V` - switch to visual mode with line highlighting
    * `ctrl+v` - switch to visual mode with verticle block highlighting

### Spellcheck

Can be defined in `~/.vimrc` with `set spell spelllang=en_us` or within
the editor using `set spell/set nospell`.

* `]s`/`[s` - go to the next/previous misspelled word
* `z=` - get suggestions for the misspelled word the cursor is on
* `zg` - mark misspelled word as correct
* `zw` - mark word as misspelled

## Workflow

### Undo & Redo

`u` - undo
`CTRL+r` - redo

### Copy & Paste

* `y` - 'yank' (copy) selection
* `yy` - yank the current line
* `p`/`P` - paste the copied (or deleted) text after/before the cursor
* `ddp` - nice shortcut to switch two lines

### Find & Replace
* `/$SEARCH` - searchs for the given search string
    * `n`/`N` - goes to the next/previous matching pattern
* `:%s /$SEARCH/$REPLACE/g` - change searched text to replace text on every line
* `:s /$SEARCH/$REPLACE/g` - change searched text to replace text on the current line

## Advance Use

Combining motions with commands provide some useful functionality,
for example:

```bash
/</div> # Search for a closing div pattern
[A]some text to append[ESC] # Append text
n. # Motion (n) + repeat command(.) now appends the text to the next found pattern.
```

### Text Objects

You can use commands to target text objects. Text objects are just
specified chunks of text.

Syntax: `$ACTION$TARGETTEXTOBJ`

Some common targets:

* `iw`/`aw` - inside/around word
* `is`/`as` - inside/around sentence
* `ip`/`ap` - inside/around paragraph
* `i"`/`a"` - inside/around double quotes
* `i'`/`a'` - inside/around single quotes
* `it`/`at` - inside/around tags
* `i$`/`a$` - inside/around a symbol (,),\[,],<,>,`,{,}

Examples using `c` command to target text objects:

* `cip` - change in paragraph
* `cis` - change in sentence
* `ci"`/`ci'` - change in double/single quotes
* `ca"`/`ca'` - change around double/single quotes (quotes deleted too)

> This pattern isn't limited to the `c` command, you can use other commands
such as `d` as well.
# Vim

Vim is a terminal based editor available in most Linux systems.

[Checkpoint (Changing Text)](https://danielmiessler.com/study/vim/)

## Basics

Vim operates in various modes that work together. Each mode handles a
different job, from normal input to processing the commands in Vim.
To better understand these commands and how they work together, it's better
to think of Vim as a language. Vim has _verbs_(actions), _nouns_(targets),
and _adverbs_ (modifiers) that it uses to construct _sentences_ (commands).

### Modes

Vim operates by using various modes:

* **Command** - Keys are interpreted as commands
    * `:w` - write changes to the file (save)
    * `:q!` - quit vim without saving changes
    * `:wq`/`ZZ` - write changes and quit
    * `:saveas $PATH` - save file to $PATH
* **Insert** - Allows for normal text input
    * `i`/`a` - switch to insert mode at/after the cursor's position
    * `I`/`A` - switch to insert mode at the beginning/end of the line
* **Visual** - Allows you to select text and apply commands to them
    * `v` - switch to visual mode with character highlighting (can be used with targeted [Text Objects](#Text%20Objects)
    * `V` - switch to visual mode with line highlighting
    * `ctrl+v` - switch to visual mode with verticle block highlighting

### Navigation

Text navigation in vim is usually handled in command mode. The arrow keys
can be used in command mode, however it is more common to use the
**h**(&#8592;), **j**(&#8595;), **k**(&#8593;), and **l**(&#8594;) keys.

Text navigation commands:

* `/$SEARCH` - search for a string ([more](#Find%20&%20Replace))
* `t`/`f` - to/find; jump cursor before/to a character
* `*` - jump cursor to other instances of the word under the cursor
* `;`/`,` - jump to the next/previous instance after jumping to a character
* `0`/`$` - jump to the beginning/end of the line
* `^` - jump to the first non-blank character in a line

Target navigation commands:

* `w`/`b` - jump to the next/previous word
* `W`/`B` - jump to the next/previous big word
* `e` - jump to the end of a word
* `)` - jump to the next sentence
* `}` - jump to the next paragraph

Screen navigation commands:

* `H`/`M`/`L` - jump to the top/middle/bottom of the _screen_
* `gg`/`G` - jump to the top/bottom of the _file_
* `CTRL+i`/`CTRL+o` - jump to previous navigation / where you were
* `CTRL+U`/`CTRL+D` - move up/down half a screen
* `CTRL+F`/`CTRL+B` - move up/down a page
* `CTRL+E`/`CTRL+Y` - move up/down one line
* `:$LINENUMBER` - jump to the given line number

### Actions (Verbs)

Actions (verbs) can be performed on various targets (nouns).

Common actions:

* `d` - delete
* `c` - change

### Modifiers (Adverbs)

Modifiers are used before targets (nouns) to describe in which way an action
will be performed.

Common modifiers:

* `i` - inside
* `a` - around
* `$NUM` - number
* `t`/`f` - to/find; searches for and stops before/at a character

### Targets (Nouns)

Targets are what an action modifies.

Common targets:

* `w` - word
* `s`/`)` - sentence
* `p`/`}` - paragraph
* `t` - tag (HTML)
* `b` - block (code)

### Commands (Sentences)

Combining these concepts, vim commands (sentences) can be constructed.

Examples:

* `d2w` - delete 2 words
* `cis` - change in sentence (delete current sentence and enter insert mode)
* `ct<` - change to < (delete text from current cursor to the '<' character)

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

### Spellcheck

Can be defined in `~/.vimrc` with `set spell spelllang=en_us` or within
the editor using `set spell/set nospell`.

* `]s`/`[s` - go to the next/previous misspelled word
* `z=` - get suggestions for the misspelled word the cursor is on
* `zg` - mark misspelled word as correct
* `zw` - mark word as misspelled

### Text Objects

You can use commands to target text objects. Text objects are just
specified chunks of text.

Syntax: `$ACTION$TARGETTEXTOBJ`

Some common targetable text objects:

* `iw`/`aw` - inside/around word
* `is`/`as` - inside/around sentence
* `ip`/`ap` - inside/around paragraph
* `i"`/`a"` - inside/around double quotes
* `i'`/`a'` - inside/around single quotes
* `it`/`at` - inside/around tags
* `i$`/`a$` - inside/around a symbol (,\[,`,{

Examples using `c` command to target text objects:

* `cip` - change in paragraph
* `cis` - change in sentence
* `ci"`/`ci'` - change in double/single quotes
* `ca"`/`ca'` - change around double/single quotes (quotes deleted too)

> This pattern isn't limited to the `c` command, you can use other commands
such as `d` as well. Along with using `t` for 'to' instead of `i` for 'in'.

### Macros

Macros allow the recording of a series of commands to be repeatable.

* `qa`/`a` - start/stop recording a marcro named 'a'.
* `@a` - playback the macro.
# nested duck arrays

There have been numerous discussions in 2021-2022 around how to deal with nested duck arrays[^1] [^2].

[^1]: https://github.com/pydata/duck-array-discussion
[^2]: https://discuss.scientific-python.org/t/creating-community-standards-for-meta-arrays-arrays-that-wrap-other-arrays/563

However, not a lot of progress has been made since then, in part because this is such a complex concept (even when limited to simple nesting).

This library is a proof of concept to show that with fairly simple methods we can already do a lot. It is deliberately designed to deal only with _simple nesting_: arrays that wrap multiple other arrays would make a already complex concept even more tricky.

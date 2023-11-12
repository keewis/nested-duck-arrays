# nested duck arrays

There have been numerous discussions in 2021-2022 around how to deal with nested duck arrays[^1] [^2].

[^1]: https://github.com/pydata/duck-array-discussion
[^2]: https://discuss.scientific-python.org/t/creating-community-standards-for-meta-arrays-arrays-that-wrap-other-arrays/563

However, nothing much came out of it, in part because this is such a complex concept (even when limited to simple nesting).

This library is a proof of concept to show that with fairly simple methods we can already do a lot. It is narrowly scoped to just simple nesting: arrays that wrap multiple arrays would make a already complex concept even more tricky.

---
title: Parsing a package.json into a Golang struct
lang: go
---

While working on [pkgpal](https://github.com/marcus-crane/pkgpal), I got stuck on how to parse package.json files.

It wouldn't be such a pain if they weren't multiple keys deep.

I don't think it was particularly difficult, I just didn't understand enough about golang was all.

Anyway, here's how I accomplished it.

```go
package main

import (
    "encoding/json"
    "fmt"
)

type PackageJson struct {
    Name string `json:"name"`
    Dependencies Dependency `json:"dependencies"`
    DevDependencies Dependency `json:"devDependencies"`
}

type Dependencies struct {
    Item Dependency
}

type Dependency map[string]interface{}

func main() {
    var pkgParsed PackageJson
    pkgJson := []byte(`{"name": "my-cool-package", "dependencies": {"coffee-script": "^4.0.0", "taekwando": "^0.1.0"}, "devDependencies": {"fresh": "^1.2.3"}}`)
    err := json.Unmarshal(pkgJson, &pkgParsed)
    if err != nil {
        panic(err)
    }
    for key, _ := range pkgParsed.Dependencies {
        fmt.Println(key)
    }
}
```
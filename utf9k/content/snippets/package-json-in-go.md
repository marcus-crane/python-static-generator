---
title: Parsing a package.json into a Golang struct
lang: go
---

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

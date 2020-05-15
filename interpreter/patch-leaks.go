// patch-leaks.go for post-processing interpreter.
// File is generated by gopy. Do not edit.
// gopy build -output=interpreter github.com/google/cel-go/interpreter
// +build ignore

package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"log"
	"os"
	"strings"
)

const (
	cStringLine = "    py_retval = Py_BuildValue((char *) \"s\", retval);"
)
var cstringFunctions = []string{
    "_wrap__interpreter_Slice_string_elem",
    "_wrap__interpreter_Slice_string_elem",

}

func isCString(line string, names []string) bool {
	for _, cfn := range names {
		if strings.HasPrefix(line, cfn) {
			return true
		}
	}
	return false
}

func patchCString(line string, out *bytes.Buffer) bool {
	out.WriteString(line)
	out.Write([]byte{'\n'})
	switch line {
	case "}":
		return false
	case cStringLine:
		out.WriteString("    free(retval);\n")
		return false
	}
	return true
}

func main() {
	file := os.Args[1]
	buf, err := ioutil.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	sc := bufio.NewScanner(bytes.NewBuffer(buf))
	obuf := &bytes.Buffer{}
	var cstring bool
	for sc.Scan() {
		line := sc.Text()
		if cstring {
			cstring = patchCString(line, obuf)
			continue
		}
		cstring = isCString(line, cstringFunctions)
		obuf.WriteString(line)
		obuf.Write([]byte{'\n'})
	}

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}

	err = ioutil.WriteFile(file, obuf.Bytes(), 0644)
	if err != nil {
		log.Fatal(err)
	}
}
 
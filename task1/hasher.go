package main

import (
  "crypto/md5"
  "encoding/hex"
)

func Main(params map[string]interface{}) map[string]interface{} {
  name := "Victor"
  course, ok := params["course"].(string)
  if !ok {
    course = "Master Project: Distributed Systems 2021"
  }
  hash := md5.Sum([]byte(course + name))
  msg := make(map[string]interface{})
  msg["hash"] = hex.EncodeToString(hash[:])
  return msg
}

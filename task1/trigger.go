package main 
import (
     "fmt"
     "net/http"
     "log"
     "time"
     "encoding/json"
 )
 
const apiAddr = "https://api.exchangerate-api.com/v4/latest/EUR"
var httpClient = &http.Client{Timeout: 15 * time.Second}

func Main(params map[string]interface{}) map[string]interface{} {
	 usdExchangeRate := getUSDExchange()
     msg := make(map[string]interface{})
     msg["EUR"] = usdExchangeRate
     msg["timestamp"] = time.Now()
     return msg
 }
 
 func getUSDExchange() string {
 	 resp, err := httpClient.Get(apiAddr)
     if err != nil {
	    log.Print(err)
     }
     defer resp.Body.Close()
     var tmp map[string]interface{}
     json.NewDecoder(resp.Body).Decode(&tmp)
     rates := tmp["rates"].(map[string]interface{})
 	 return fmt.Sprintf("%f", rates["USD"])
 }

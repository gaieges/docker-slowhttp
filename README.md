# Slow container simulator

Simple little tool that allows you to test out liveness probes, or other latency related things in a container

Starts up a http server on port 8000, and responds to get requests on `/` slow 10% of the time.  Slow is defined as 5s

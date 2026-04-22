from server import BugGrpcServerStub


def demo_client_flow() -> None:
    server = BugGrpcServerStub()
    bug_id = server.CreateBug("PIS-API", "Race condition in upload", "CRITICAL")
    bug = server.GetBug(bug_id)
    stream = server.ListActiveBugs("PIS-API")
    print("Created:", bug)
    print("Stream count:", len(stream))


if __name__ == "__main__":
    demo_client_flow()

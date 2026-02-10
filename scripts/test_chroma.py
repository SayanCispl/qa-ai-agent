from src.vector_store import VectorStore

vs = VectorStore()

vs.add(
    text="Login page should allow valid users to log in",
    metadata={"type": "requirement"},
    doc_id="req_login_1"
)

vs.add(
    text="Test login with valid username and password",
    metadata={"type": "test_case"},
    doc_id="tc_login_1"
)

results = vs.search("login test case")

print("Search Results:")
for r in results:
    print("-", r)

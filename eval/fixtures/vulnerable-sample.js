// FIXTURE — intentionally vulnerable sample for security-skill testing.
// Every secret below is FAKE. Never replace with real credentials.
const PUBLIC_AWS_KEY_EXAMPLE = "AKIAIOSFODNN7EXAMPLE";      // AWS docs example key
const STRIPE_TEST_TOKEN = "sk_test_FAKEKEY000000000000";     // stripe test-mode placeholder

function unsafeQuery(conn, userId) {
  // SQL built by concatenation — nuclei/zap-style review must flag this
  return conn.query("SELECT * FROM users WHERE id = " + userId);
}

function unsafeRender(req, res) {
  // XSS sink — clean-code gate must BLOCK
  res.send("<h1>Hello " + req.params.name + "</h1>");
}

module.exports = { unsafeQuery, unsafeRender };

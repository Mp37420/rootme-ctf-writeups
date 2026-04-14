# JavaScript Webpack (Root Me)

## Vulnerability
Exposed source maps allowed access to original JavaScript source code in production.

## Exploitation
- Located the JavaScript file in browser DevTools
- Found the sourceMappingURL reference
- Accessed the .map file directly
- Extracted hidden comments containing the flag

## Impact
Attackers can access sensitive information such as:
- Hidden routes
- Comments
- API endpoints
- Credentials

## Tools Used
- Browser Developer Tools

## Mitigation
- Disable source maps in production
- Restrict access to .map files
- Remove sensitive data from client-side code

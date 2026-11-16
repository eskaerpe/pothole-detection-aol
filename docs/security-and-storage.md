# Security, privacy and storage

## Boundaries
Private uploads/evidence are not static/public assets. Use opaque references and authorization checks for every admin/media route; reject traversal and unsafe filenames. No public personal name/contact fields are required. Explain consent/use of video and retention; keep faces/plates/private locations out of public artifacts and logs.

## Upload and decoding
Validate metadata, container/codec via actual probing rather than extension alone, byte/duration limits, truncated/corrupt files and supported decode path. PRD's proposed 100 MB/60-second MP4 H.264 limits require phase 01 approval and real phase 05 validation. Enforce bounded streaming, temporary-file finalization, timeouts/frame limits and safe failure cleanup. No shell interpolation of user input. Upload and selection never launch inference.

## Admin and web
Store password hashes, not plaintext. Configure secrets outside Git, secure session lifecycle/expiry, CSRF on state-changing actions, appropriate cookie flags for the approved deployment mode, safe template escaping and bounded login/upload abuse protection. Single-host demo does not justify unrestricted media access or default public credentials. Specify session/rate-limit policy before shipping.

## Capacity and failure
Check free capacity before and during writes; test disk-full and permission failures, temporary leftovers and DB/file consistency. Define retention and capacity limits with owner approval; no silent deletion. Protect originals and successful attempts. Interrupted decode/worker state must be inspectable and recoverable without double counting.

## Backup/restore
Back up consistent DB state plus referenced private media/config needed for restoration, without exposing secrets. SQLite WAL/live copying needs a supported consistent backup strategy. In an isolated approved destination, verify every expected source artifact by hash and actually restore/query/view representative records/media. Matching hashes alone do not prove restoreability. Never overwrite source data during a restore drill.

## Release boundary
No public deployment, purchases, external uploads or security guarantees are implied by local tests. The final report names which controls were exercised and which were only designed. See [test matrix](testing-and-acceptance.md).

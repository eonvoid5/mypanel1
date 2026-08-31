# VOID HOST — Build Specification

## Core rule
VOID HOST keeps the familiar Pterodactyl/Jexactyl information architecture and control placement, while using an original visual system: shader-packed Minecraft scenery, frosted glass, soft blur, rounded surfaces, subtle glow, depth, and smooth motion.

## Server/client navigation target
- Overview / Dashboard
- My Servers / Servers
- Server Console
- Files / File Manager
- Databases
- Schedules
- Users / Sub-Users
- Backups
- Network / Allocations
- Startup
- Settings
- Activity / Audit
- Plugin Manager
- Mod Manager
- Modpack Manager

## Admin target
- Overview
- Servers
- Nodes / Wings
- Locations
- Allocations / Ports
- Users
- Nests
- Eggs
- Mounts
- API Keys
- Settings
- Activity / Audit
- System / Queue / Telemetry

## Jexactyl-style additions to preserve as feature targets
- Billing and resource purchasing
- Stripe / PayPal billing target
- Server renewal flow
- User approvals
- Ticket/support system
- Referral/reward concepts
- Admin configuration controls
- Plugin management
- Advanced per-instance metrics

## Server page target
Top server identity/action bar:
- server name
- online/offline state
- address and port
- Start / Restart / Stop / Kill

Primary tabs:
- Console
- Files
- Databases
- Schedules
- Users
- Backups
- Network
- Startup
- Settings
- Activity

Management shortcuts:
- Plugin Manager
- Mod Manager
- Modpack Manager
- Pro Tools

## Visual system
- Full-screen Minecraft shader-style forest/world background
- Dark green/black cinematic overlay for readability
- Frosted translucent cards with 20–32px blur
- 16–28px rounded corners
- Fine 1px low-opacity borders
- Soft green/cyan/purple accent glow used sparingly
- Floating cards with layered depth and gentle hover lift
- Animated live telemetry lines and meters
- Glass sidebar and glass topbar
- Responsive desktop/tablet/mobile layouts
- Respect reduced-motion preferences

## Engineering rule
UI must remain functional, not a static mockup. Tabs, buttons, search, server actions, forms, dialogs, tables, console controls, and navigation should have real state and validation. Backend integrations should be separated from presentation so the UI can later connect to Pterodactyl/Wings APIs.

## Reference research
Pterodactyl is a complex self-hosted game-server management panel with a PHP/React panel and Wings daemon architecture. Its official documentation covers installation, queues, telemetry, backups, reverse proxy, 2FA, and related infrastructure.

Jexactyl is a feature-rich Pterodactyl fork focused on game-server management plus billing. Current project materials describe integrated Stripe/PayPal billing, user/server purchasing, server renewals, approvals, customizable administration, plugin management, and enhanced metrics.

## Build priority
1. Preserve information architecture and controls.
2. Replace visual language with VOID HOST glass/shader design.
3. Build complete client server-management shell.
4. Build admin shell.
5. Add Jexactyl feature targets.
6. Connect real APIs/backend.
7. Test permissions, loading, errors, empty states, mobile layout, and destructive actions.

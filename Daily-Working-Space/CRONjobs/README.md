# CRON Jobs

Automated tasks running on the OpenClaw gateway.

## Active Cron Jobs

| Time (UTC) | Schedule | Description |
|------------|----------|-------------|
| 00:30 | Daily | Daily growth resources automation |
| 06:00 | Daily | Morning automation check |
| 08:30 | Days 2-6 | Content generation (Mon-Fri) |
| 09:00 | Days 2-6 | Mid-morning content pipeline |
| 16:30 | Days 2-6 | Afternoon content push |

## Cron Log Locations

- `/home/itsaslamautomations/.openclaw/workspace/Daily-Working-Space/.cron_log.txt`
- `/tmp/daily_growth.log`
- `/tmp/content_cron.log`

## Scripts

- `daily_growth_resources.sh` - Growth automation
- `generate_content.sh` - Content generation
- `daily_implementation.sh` - Daily implementation tasks

---

*Last Updated: March 22, 2026*

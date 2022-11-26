# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "5044292"))
API_HASH = os.getenv("API_HASH", "0d1889497b7e7f1717cef2f8ddaae361")
SESSION = os.getenv("SESSION", "BQAYpTAAhadMCOZa7zWwjbjpRcko_A6x65XKjFFfytGc7y5c1W_wgZUL4mol_T98fsLwwOYpqAOuI6CY3eb5ULsa9A82c6NO8SaOMZDRhsKEEIPlzMk6CbPI_eI4gEF-C8oqjEjftuhtZzkft7BDY1684DVptUwXEf5oq5vHaRHpRo_5UJPYRm6_lFbO14BXeDlDlpl0M0j0IjEIymbl4UV3YEENpmSzRD5F1vt-b6XXykaviV4pLdnZLL1EbQQWw7t1uGFsEnqHFogIQqt4U2BGRWBKDBlf_AgZ-SAiNlmwJu8fgFN1TlNm25Y91VMmemwp1H_eTWekFFw8vSPtBtNQf23ljQAAAAFJy_HbAA")
OWNER = os.getenv("OWNER", "FOUNDER_OF_UNC")
SUPPORT = os.getenv("SUPPORT", "TEAM_HEARTLESS_POLICE_OP")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5274117736").split()))

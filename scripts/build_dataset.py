#!/usr/bin/env python3
"""Convert the 2026-09-11 Bitcoin Puzzle dossier to CAUDO's public-safe index."""
import argparse, json, pathlib, urllib.request, zipfile, io, collections
URL="https://archive.org/download/btcpuzzle-data-2026-09-11/btcpuzzle-data-2026-09-11.json"
FIELDS=("puzzle_id","category","created_at","announced_at","address","funding_txid","reward_btc","status","source_url","solution_evidence","github_repos","last_verified_at")
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",default="");p.add_argument("--output",default="data/puzzles.json");a=p.parse_args()
 if a.input:
  raw=pathlib.Path(a.input).read_bytes()
  if zipfile.is_zipfile(io.BytesIO(raw)):
   with zipfile.ZipFile(io.BytesIO(raw)) as z: raw=z.read("btcpuzzle-data-2026-09-11.json")
 else:
  with urllib.request.urlopen(urllib.request.Request(URL,headers={"User-Agent":"CAUDO-research-index/1.0"}),timeout=70) as response:raw=response.read()
 doc=json.loads(raw);rows=doc["puzzles"];assert len(rows)==256
 result=[]
 for x in rows:
  solved=x.get("solved") is True
  evidence={"spend_txid":x["out_largest_txid"],"spend_block":x.get("out_largest_block")} if solved and x.get("out_largest_txid") else None
  # "verified" here means internally corroborated by this community dataset, NOT independently chain-verified.
  status="solved-claimed" if solved else ("unspent" if (x.get("balance_sat") or 0)>0 else "unknown")
  v=dict(puzzle_id=f"BTC-{x['puzzle']:03d}",category="Bitcoin Puzzle 256",created_at=x.get("creation_time_utc"),announced_at=None,address=x.get("address_compressed"),funding_txid=x.get("creation_txid"),reward_btc=None,status=status,source_url="https://archive.org/details/btcpuzzle-data-2026-09-11",solution_evidence=evidence,github_repos=[],last_verified_at=x.get("balance_checked_utc"))
  v.update(puzzle_number=x["puzzle"],difficulty_bits=x["bits"],creation_vout=x.get("creation_vout"),funding_2015_sat=x.get("funding_2015_sat"),funding_2017_sat=x.get("funding_2017_sat"),funding_2023_sat=x.get("funding_2023_sat"),balance_sat_snapshot=x.get("balance_sat"),solved_in_source=solved)
  result.append(v)
 dest=pathlib.Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps({"metadata":{"source":"btcpuzzle-data-2026-09-11.json","source_built_utc":doc["_about"]["built_utc"],"record_count":256,"note":"No private keys, WIF, nonce data; classification from source, not independent verification."},"puzzles":result},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print("Wrote",dest,collections.Counter(r["status"] for r in result))
if __name__=="__main__":main()

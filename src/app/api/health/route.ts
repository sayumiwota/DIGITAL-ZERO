import { NextResponse } from "next/server";
import { buildHealthSnapshot } from "@/lib/health";

export const dynamic = "force-dynamic";

export function GET() {
  return NextResponse.json(buildHealthSnapshot(), {
    status: 200,
    headers: {"Cache-Control": "no-store"},
  });
}

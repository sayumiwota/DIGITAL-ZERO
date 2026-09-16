import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "DIGITAL ZERØ | Engineering Control Center",
  description: "Autonomous Software Engineering Factory control surface for DIGITAL ZERØ.",
};

export default function RootLayout({children}: Readonly<{children: React.ReactNode}>) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}

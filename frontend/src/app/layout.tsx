import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
    title: 'DATA 3 - Projet 1',
    description: 'Générateur de chiffres manuscrits',
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="fr-FR">
            <body className={inter.className}>{children}</body>
        </html>
    );
}

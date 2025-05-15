// lib/prisma.ts
import { PrismaClient } from '@/generated/prisma'

// Create a place to hang the client on `global` in dev so we don't get timeouts
declare global {
  // eslint-disable-next-line no-var
  var prisma: PrismaClient | undefined
}

const prisma =
  global.prisma ||
  new PrismaClient({
    log: ['query'],
  })

if (process.env.NODE_ENV !== 'production') {
  global.prisma = prisma
}

export default prisma

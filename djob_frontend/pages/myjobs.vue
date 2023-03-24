<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">My jobs</h1>

        <div class="space-y-4">
            <Job :my="true" />

            <Job :my="true" />

            <Job :my="true" />
        </div>
    </div>
</template>
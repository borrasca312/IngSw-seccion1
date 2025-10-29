import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import StatCard from './StatCard.vue'

describe('StatCard.vue', () => {
  it('renders correctly', () => {
    const wrapper = mount(StatCard, {
      props: {
        title: 'Test Title',
        stat: '123',
        change: '+10%',
      },
    })
    expect(wrapper.exists()).toBe(true)
  })
})
